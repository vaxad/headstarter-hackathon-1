import { Inter } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/ui/theme-provider"
import Navbar from "@/components/custom-ui/Navbar";
import { Toaster } from "@/components/ui/sonner"
import AuthChecker from "@/components/custom-ui/AuthChecker";
import { Suspense } from "react";
import { GoogleAnalytics } from '@next/third-parties/google'

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
	title: "Blitz AI",
	description: "Automate your content creation.",
};

export default function RootLayout({ children }) {
	return (
		<html lang="en">
			<body id="style-2" className={inter.className}>
				<AuthChecker />
				<ThemeProvider
					attribute="class"
					defaultTheme="system"
					enableSystem
					disableTransitionOnChange>
					<Navbar />
					<div className=" ml-64 mt-20">
						<Suspense>
							{children}
						</Suspense>
						<Toaster />
					</div>
				</ThemeProvider>
			</body>
			<GoogleAnalytics gaId="G-NV93ESXKSC" />
		</html>
	);
}
