# glauberxyz/modulato

⭐ 10 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/glauberxyz/modulato) · [官网](https://modulato.dev) · 个人维护

**面向网站制作的动效优先 React 框架，人和 LLM 皆可用**

以视觉设计为先的 React 网站框架：页面切换时新旧页面共存（crossfade/slide/FLIP 共享元素），菜单、光标、WebGL 等置于持久化且 URL 感知的 shell 中；动效参数以 motion.ts token 形式存储，可在 dev overlay 中实时调整并保留 AST 写回，支持断点响应、reduced-motion，且可被 agent 通过 MCP 编辑。包含 SSR + hydration，可部署到 Vercel。以脚手架命令创建项目，发布为多个 npm 包（runtime、vite 构建、SSR 服务器、GSAP 封装、WebGPU/WebGL shader、dev overlay、MCP server、脚手架器）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页面切换期间新旧页面共存，支持 crossfade、slide 与 FLIP 共享元素
- motion.ts 动效 token 可实时调整并 AST 保留写回，支持断点与 reduced-motion
- agent 可通过 MCP 编辑动效 token（@modulato/mcp）
- @modulato/gpu 支持 WGSL/WebGPU 与 GLSL/WebGL2 的热切换 shader

## 适用场景

- 制作以转场动画为核心的展示型网站
- 在 dev overlay 中实时微调动效参数并保存回代码
- 让 AI agent 通过 MCP 修改站点动效配置

## 场景标签

 · 领域:Web 开发/前端框架

## 证据(README 行号)

> L9: custom transitions and animations. Built for humans and LLMs alike.
> L21:  reduced-motion aware, editable by agents over MCP.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `64c1e8e0044e` · [字段定义](../../DATASET.md)*
