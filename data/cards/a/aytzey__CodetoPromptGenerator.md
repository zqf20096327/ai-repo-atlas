# aytzey/CodetoPromptGenerator

⭐ 18 · TypeScript · MIT · 推送 2026-07-08 · [GitHub](https://github.com/aytzey/CodetoPromptGenerator) · 个人维护

**把本地代码库一键组装成 LLM 提示词的桌面应用**

基于 Electron + Next.js + Flask 的跨平台桌面应用，面向需要将代码库喂给大模型的开发者：扫描本地文件树生成项目结构，可勾选/排除文件与目录，统计 token 用量，管理 meta prompt，一键复制包含文件内容的完整提示词到剪贴板。AI 部分为经 OpenRouter API 调用 LLM 的智能文件选择与提示词精炼（需自备 API key）。附带看板、待办与用户故事管理。从源码克隆并运行 setup.sh 安装，也可用 electron-builder 打包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Tree-sitter 代码地图与递归文件树导航
- 文件/目录勾选与排除管理，实时显示 token 统计
- 经 OpenRouter 的 LLM 智能文件选择与提示词精炼（需 API key）
- Electron 跨平台，可打包 .deb/.AppImage 分发包

## 适用场景

- 把整个或部分代码库整理成提示词粘贴给 LLM 做分析或改写
- 控制送给 LLM 的上下文范围并监控 token 消耗
- 复用与维护常用 meta prompt 模板

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Turn any codebase into an LLM-ready prompt in one click — Tree-sitter code maps plus LLM-driven smart file selecti
> L7: A tool for quickly assembling Large Language Model (LLM) prompts from a local file tree. You can select or exclude s
> L19: - **AI-Powered Features**: Smart file selection and prompt refinement using LLMs (requires OpenRouter API key).

## 星数曲线

```mermaid
xychart-beta
    title "aytzey/CodetoPromptGenerator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `efbeee8eccc7` · [字段定义](../../DATASET.md)*
