import { io } from 'socket.io-client'

const URL = process.env.NODE_ENV === 'production' ? undefined : "http://backend:8080";

export const socket = io(URL)