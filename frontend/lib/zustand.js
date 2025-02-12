import { create } from "zustand";

const store = create((set) => ({
	backend_url: process.env.NEXT_PUBLIC_BACKEND_URL,
	api: "b0fb7836d4864aae85d180a8e8fd6020",
	message: "",
	setMessage: (item) => set(() => ({ message: item })), // set is a function that takes a function
	type: "info",
	setType: (item) => set(() => ({ type: item })),
	toast: false,
	setToast: (item) => set(() => ({ toast: item })),
	user: null,
	setUser: (item) => set(() => ({ user: item })),
	auth: true,
	setAuth: (item) => set(() => ({ auth: item })),
	Logout: () => set(() => ({ user: null, auth: false })),
	getUser: (token) => set(async () => ({ user: await getMe(token) })),
	demoEnv: false,
	demoDelayMs: 2000
}));

const getMe = async (token) => {
	const url = process.env.NEXT_PUBLIC_BACKEND_URL
	const res = await fetch(`${url}/auth/me`, {
		method: "GET",
		headers: {
			"Content-Type": "application/json",
			"auth-token": token
		}
	})
	const data = await res.json()
	if (!data.error) {
		return data.user
	} else {
		return null
	}
}

export default store;