/**
 * @jest-environment jsdom
 */

const path = require("path");
const fs = require("fs");

jest.spyOn(window, "alert").mockImplementation(() => {});

beforeAll(() => {
  const filePath = path.resolve(__dirname, "../../../templates/base.html");
  const fileContents = fs.readFileSync(filePath, "utf8");
  document.body.innerHTML = fileContents;
  ({ banner, closeButton } = require("../index"));
});

describe("banner closes on dismiss", () => {
  test("banner is removed from DOM", () => {
    closeButton.click();
    expect(banner.style.display).toBe("none");
  });
});
