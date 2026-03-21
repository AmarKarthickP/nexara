import frappe from "frappejs"; // or window.frappe if global

export async function callAPI(method, args = {}) {
  try {
    const res = await frappe.call({
      method,
      args
    });

    return res.message;
  } catch (err) {
    console.error("API Error:", err);
    throw err;
  }
}