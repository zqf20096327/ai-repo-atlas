# imMatheus/spidey-sense

⭐ 41 · TypeScript · MIT · 推送 2026-07-21 · [GitHub](https://github.com/imMatheus/spidey-sense) · [官网](https://www.npmjs.com/package/spidey-sense) · 个人维护

**给 React 开发者：在本地网页上点选元素、用自然语言驱动 AI 改源码**

面向本地 React 应用的开发工具：通过 Vite 插件或 Next.js 包装器注入运行时，在开发页面上点选任意元素、输入自然语言修改需求，由本地 claude CLI（或 codex CLI）作为 agent 直接编辑磁盘上的源码文件，元素显示彩色轮廓与状态徽章，多任务并行。也提供脱离打包器的独立 CLI，手动粘贴 script 标签使用。要求 Node 18+、本地 claude CLI 在 PATH 上、React 开发构建（依赖 _debugSource 源码映射，仅 dev 生效，不进入生产构建）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 页面元素点选 + 自然语言 prompt，agent 直接改写磁盘源码
- Vite 插件 / Next.js 包装器 / 独立 CLI 三种接入方式
- 多任务并行运行，元素带彩色轮廓与状态徽章
- 仅 dev 环境注入，生产构建不包含运行时

## 适用场景

- 前端开发时对着页面直接描述改动，让 AI 改源码
- 在 Vite 或 Next.js 项目中快速集成可视化 AI 编辑
- 无支持打包器的项目（Webpack/CRA/Parcel）用独立 CLI 接入

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Vibe code from your website. Click any element in your local React app, ask for your change, get Claude or Codex to 
> L61: 4. The element keeps a colored outline + status badge while a Claude agent runs.
> L67: - The local `claude` CLI on PATH (or pass `claudeBin` to the plugin).

## 星数曲线

```mermaid
xychart-beta
    title "imMatheus/spidey-sense 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0aab4f1cf0ea` · [字段定义](../../DATASET.md)*
