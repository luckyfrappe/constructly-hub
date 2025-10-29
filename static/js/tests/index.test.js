/**
 * @jest-environment jsdom
 */

jest.spyOn(window, "alert").mockImplementation(() => {});

beforeAll(() => {
  let fs = require("fs");
  let fileContents = fs.readFileSync("base.html", "utf8");
  document.body.innerHTML = fileContents;
  ({ banner, closeButton } = require("../index"));
});

describe("banner closes on dismiss", () => {
  test("banner is removed from DOM", () => {
    closeButton.click();
    expect(banner.style.display).toBe("none");
  });
});
