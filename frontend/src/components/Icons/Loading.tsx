export default function Loading({ className }: { className: string }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      id="Isolation_Mode"
      data-name="Isolation Mode"
      viewBox="0 0 24 24"
      className={`${className} animate-spin`}
    >
      <path
        fill="currentColor"
        d="M.415,12.051a12,12,0,0,1,23.17-4.364L20.791,8.779a9,9,0,1,0,0,6.545l2.794,1.092A12,12,0,0,1,.415,12.051Z"
      />
    </svg>
  );
}
