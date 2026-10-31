# gojodennis/OpenKombai

⭐ 23 · TypeScript · MIT · 推送 2025-12-16 · [GitHub](https://github.com/gojodennis/OpenKombai) · [官网](https://openkombai.vercel.app) · 个人维护

**本地 LLM 将截图/设计稿转为 React+Tailwind 代码的工具**

开源的设计转代码工具：通过 Ollama 运行本地模型（Llama 3.2 Vision、Qwen 2.5 Coder），把截图与设计文件生成为 React + Tailwind CSS + Lucide Icons 代码。设计文件不上传，无需 API key。后端为 Python FastAPI + Pillow，前端为 React + Vite + Shadcn UI，提供拖放截图并预览代码的 Studio 界面。Ollama 需另行安装并拉取模型，要求 Python 3.10+ 与 Node.js 18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Ollama 的本地 LLM（Llama 3.2 Vision、Qwen 2.5 Coder）生成代码
- 无需 API key，设计文件不上传机器
- 生成 React + Tailwind CSS + Lucide Icons
- React 拖放式 Studio 界面用于上传截图与预览代码

## 适用场景

- 把 UI 截图或设计稿快速转成 React + Tailwind 代码
- 在不连接云端 API 的前提下做前端原型生成
- 希望设计数据留在本地的开发流程

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: > **Free, Local, Open Source AI Frontend Generator.** (Alternative to Kombai)
> L5: OpenKombai is an open-source tool that turns **Screenshots** and **Design Files** into production-ready **React + Ta
> L9: - **Zero Cost**: Built on top of local LLMs (Llama 3.2 Vision, Qwen 2.5 Coder) via Ollama.

## 星数曲线

```mermaid
xychart-beta
    title "gojodennis/OpenKombai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-31 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `688539803e16` · [字段定义](../../DATASET.md)*
