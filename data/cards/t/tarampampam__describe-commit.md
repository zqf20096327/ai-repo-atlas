# tarampampam/describe-commit

⭐ 27 · Go · MIT · 推送 2026-10-11 · [GitHub](https://github.com/tarampampam/describe-commit) · 个人维护

**CLI 工具：基于 Git 变更用 AI 生成提交信息**

命令行工具，读取指定 Git 仓库的 git diff（可选 git log）发送给 AI 提供商，生成符合规范的 commit message。支持 OpenAI、Gemini、OpenRouter、Anthropic 四个提供商，可切换模型，也可通过自定义 base URL 接入 Ollama、LM Studio、vLLM 等 OpenAI 兼容端点。以独立二进制运行（仅需已安装 git），提供 .deb/.rpm/AUR 安装、跨平台二进制与 Docker 镜像，支持 YAML 配置与 git alias 集成。README 提示代码会发送给 AI 提供商，专有代码使用需注意公司政策。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 git diff/log 后交由 AI 生成 commit message
- 支持 OpenAI/Gemini/OpenRouter/Anthropic，可选模型与自定义 base URL
- 可接入 Ollama、LM Studio、vLLM 等 OpenAI 兼容本地端点
- 独立二进制运行（仅需 git），提供 deb/rpm/AUR/二进制/Docker 多种分发

## 适用场景

- 我不想手写 commit message，让 AI 根据改动直接生成
- 把工具注册为 git alias，一条命令完成暂存与提交
- 通过 Ollama 等本地模型生成提交信息，避免代码外发
- 为特定项目定制 emoji 或仅主题行的简短提交信息

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: `describe-commit` is a CLI tool that leverages AI to generate commit messages based on changes made in a Git reposit
> L44: > - Sends this diff to the AI provider with the provided special prompt

## 星数曲线

```mermaid
xychart-beta
    title "tarampampam/describe-commit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `24568751986d` · [字段定义](../../DATASET.md)*
