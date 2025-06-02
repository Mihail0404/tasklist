export type Task = {
  id: number;
  name: string;
  description: string;
  ownerId: number;
  createdAt: Date;
  completedAt: Date | null;
};
