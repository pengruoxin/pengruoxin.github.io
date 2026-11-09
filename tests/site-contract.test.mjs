import assert from "node:assert/strict";
import { existsSync, mkdirSync, rmSync, readFileSync, statSync } from "node:fs";
import { spawnSync } from "node:child_process";
import test, { before } from "node:test";

const outputDirectory = ".tmp/site-contract";
const restrictedPublicPhrases = [
  "RGVSeQ==",
  "TGF5ZXItU1dBUCBTcXJ0",
  "UjA1",
  "UjA2",
  "UjA3",
  "UjA4",
  "UjA5",
  "ZG91YmxlLWJsaW5k",
  "ZG91YmxlIGJsaW5k",
  "dW5kZXIgcmV2aWV3",
].map((value) => Buffer.from(value, "base64").toString("utf8"));
const restrictedPublicPattern = new RegExp(restrictedPublicPhrases.map((value) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join("|"), "i");

function buildSite() {
  rmSync(outputDirectory, { recursive: true, force: true });
  mkdirSync(".tmp", { recursive: true });
  const result = spawnSync(
    "bundle",
    ["exec", "jekyll", "build", "--config", "_config.yml,tests/fixtures/test.yml", "--destination", outputDirectory],
    { encoding: "utf8", env: { ...process.env, JEKYLL_ENV: "production" } }
  );

  assert.equal(result.status, 0, `Jekyll build failed.\nSTDOUT:\n${result.stdout}\nSTDERR:\n${result.stderr}`);
}

before(() => {
  buildSite();
});

test("tracked public source does not contain restricted terminology", () => {
  const trackedFiles = spawnSync("git", ["ls-files", "-co", "--exclude-standard"], { encoding: "utf8" }).stdout.trim().split("\n").filter(Boolean);

  for (const file of trackedFiles) {
    if (!existsSync(file) || !statSync(file).isFile()) continue;
    const contents = readFileSync(file);
    if (contents.includes(0)) continue;
    assert.doesNotMatch(contents.toString("utf8"), restrictedPublicPattern, `restricted terminology found in ${file}`);
  }
});

test("the rendered homepage identifies Peng Ruoxin and exposes verified academic links", () => {
  const homepage = readFileSync(`${outputDirectory}/index.html`, "utf8");

  assert.match(homepage, /Peng Ruoxin/);
  assert.match(homepage, /https:\/\/pengruoxin\.github\.io/);
  assert.match(homepage, /https:\/\/github\.com\/pengruoxin/);
  assert.match(homepage, /scholar\.google\.com\/citations\?user=SluSJCYAAAAJ/);
  assert.match(homepage, /mailto:yiwu1777@gmail\.com/);
  assert.match(homepage, /href="[^"]*peng-ruoxin-cv\.pdf"/);
  assert.doesNotMatch(homepage, /You R\. Name|you@example\.com|Example University/);
});

test("the homepage explains the research area before presenting HeteroWeave", () => {
  const homepage = readFileSync(`${outputDirectory}/index.html`, "utf8");
  const categoryPosition = homepage.indexOf("Vision Model Reassembly");
  const projectPosition = homepage.indexOf("HeteroWeave");

  assert.ok(categoryPosition >= 0, "the public research category is missing");
  assert.ok(projectPosition > categoryPosition, "HeteroWeave appears before its research category is explained");
  assert.match(homepage, /Research Interests/);
  assert.match(homepage, /Selected Publications/);
  assert.match(homepage, /Education/);
});

test("the featured research page presents public HeteroWeave evidence without restricted terminology", () => {
  const researchPage = readFileSync(`${outputDirectory}/research/heteroweave/index.html`, "utf8");

  assert.match(researchPage, /HeteroWeave/);
  assert.match(researchPage, /CLAS/);
  assert.match(researchPage, /0\.775/);
  assert.match(researchPage, /0\.570/);
  assert.match(researchPage, /79\.457%/);
  assert.match(researchPage, /26\.7%/);
  assert.match(researchPage, /11\.9%/);
  assert.match(researchPage, /serial single-block reassembly/i);
  assert.doesNotMatch(researchPage, restrictedPublicPattern);
});

test("the research index presents HeteroWeave as the category-first main project", () => {
  const researchIndex = readFileSync(`${outputDirectory}/research/index.html`, "utf8");

  assert.match(researchIndex, /Vision Model Reassembly/);
  assert.match(researchIndex, /Main Project/);
  assert.match(researchIndex, /HeteroWeave/);
  assert.match(researchIndex, /CLAS/);
  assert.match(researchIndex, /79\.457%/);
  assert.doesNotMatch(researchIndex, restrictedPublicPattern);
});

test("the publications page contains the three verified research outputs", () => {
  const publications = readFileSync(`${outputDirectory}/publications/index.html`, "utf8");

  assert.match(publications, /An Overall Real-Time Mechanism for Classification and Quality Evaluation of Rice/);
  assert.match(publications, /An Improved Pure Fully Connected Neural Network for Rice Grain Classification/);
  assert.match(publications, /Intelligent Recognition of Live Pig Aggregation Behavior Based on Convolutional Neural Network/);
  readFileSync(`${outputDirectory}/assets/pdf/peng-ruoxin-cv.pdf`);
});

test("the experience page summarizes verified research and technical work", () => {
  const homepage = readFileSync(`${outputDirectory}/index.html`, "utf8");
  const experience = readFileSync(`${outputDirectory}/experience/index.html`, "utf8");

  assert.match(homepage, /href=["']\/experience\/["']/i);
  assert.match(experience, /Research Experience/);
  assert.match(experience, /HeteroWeave/);
  assert.match(experience, /Rice Classification and Quality Evaluation/);
  assert.match(experience, /Pig Aggregation Behavior/);
  assert.match(experience, /Yuyi Robot/);
  assert.match(experience, /Jetson AGX Orin/);
  assert.doesNotMatch(experience, restrictedPublicPattern);
});

test("the rendered site exposes the responsive and accessible academic visual system", () => {
  const homepage = readFileSync(`${outputDirectory}/index.html`, "utf8");
  const stylesheet = readFileSync(`${outputDirectory}/assets/css/academic.css`, "utf8");

  assert.match(homepage, /<meta[^>]+name=["']viewport["'][^>]*>/i);
  assert.match(homepage, /href=["'][^"']*\/assets\/css\/academic\.css[^"']*["']/i);
  assert.match(homepage, /class=["'][^"']*skip-link[^"']*["'][^>]*href=["']#main-content["']/i);
  assert.match(homepage, /id=["']main-content["']/i);
  assert.match(homepage, /id=["']research-interests["']/i);
  assert.match(homepage, /id=["']featured-research["']/i);
  assert.match(homepage, /id=["']publications["']/i);
  assert.match(homepage, /id=["']education["']/i);
  assert.match(homepage, /href=["']\/research\/["']/i);

  assert.match(stylesheet, /:focus-visible/);
  assert.match(stylesheet, /prefers-reduced-motion:\s*reduce/);
  assert.match(stylesheet, /@media\s*\([^)]*max-width/i);
});
