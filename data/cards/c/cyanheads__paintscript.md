# cyanheads/paintscript

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/cyanheads/paintscript) · [官网](https://www.npmjs.com/package/paintscript) · 个人维护

**让 AI 模型用 JavaScript 脚本模拟真实颜料作画的引擎**

Paintscript 提供一个模拟画布，以 passage 为单位的 JavaScript 脚本混色、装笔、落笔，颜料行为基于 Kubelka–Munk 模型，支持油画厚涂、水墨与水彩等质感，笔触由多毛刷束生成条纹与堆叠。每次运行原子提交，失败按瓦片回滚；脚本与日志可在新画布上逐字节复现画作，并渲染为延时 GIF。API 显式面向 AI 模型设计（vocabulary 输出可放入 prompt 的 TypeScript 声明），同时也供人工编写。需 Node ≥22 或 Bun，沙箱为 WebAssembly 的 QuickJS，无原生构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Kubelka–Munk 模型的颜料混色、覆盖与罩染模拟
- 脚本+journal 精确重放，同一 seed 逐字节复现画作并生成延时 GIF
- 原子运行、瓦片级撤销与 time/strokes/memory 预算限制
- paintscript vocabulary 输出供模型 prompt 使用的 API 声明

## 适用场景

- 让 AI agent 通过脚本 API 在模拟画布上作画
- 生成数字绘画 PNG 与作画过程延时 GIF
- 需要可复现的生成艺术与创意编码实验

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: The paint behaves like real paint. Colors mix the way pigments do, so blue and yellow make green; opaque paint cover
> L2:  Paint by code: JavaScript lays simulated brush strokes, from thick oil paint to ink and watercolor-like washes, sav
> L140: npm install paintscript


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f3046500cef2` · [字段定义](../../DATASET.md)*
