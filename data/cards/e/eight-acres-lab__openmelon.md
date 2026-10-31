# eight-acres-lab/openmelon

⭐ 89 · Go · Apache-2.0 · 推送 2026-05-11 · [GitHub](https://github.com/eight-acres-lab/openmelon) · [官网](https://pointeight.ai) · 组织维护 · 中文 README

**终端内容创作 agent：以项目为单位多模态生成图文**

运行在终端的 TUI 内容创作 agent。每个项目将角色、参考素材与生成产物保存在磁盘，LLM 借助工具注册表（角色/参考/创作空间检索、bash 等）在项目上下文内起草，使同一角色形象跨会话保持一致。安装为 npm 全局包（下载 Go 二进制并校验哈希），也可 go install 从源码构建。支持 OpenRouter / OpenAI / Anthropic 供应商，bash 工具有三级权限门控，会话可 resume 且原始记录不可变，检索采用 grep 而非向量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 项目制持久上下文：角色、参考与产物保存在磁盘，角色形象跨会话锚定
- TUI 命令面板 + headless 模式（openmelon -p）支持脚本与子 agent 集成
- bash 工具三级权限模式（strict/auto/trusted）与 Judge LLM 门控
- 会话记录不可变，openmelon resume 可在新目录续接对话

## 适用场景

- 我在终端里持续为同一批角色生成图文内容并保持形象一致
- 通过脚本或子 agent 无头调用同一套创作栈
- 为 Claude Code / Cursor 挂载该工具作为内容生成后端

## 场景标签

`多模态` `图像生成` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3:  A content-creation agent that runs in your terminal.
> L5: OpenMelon turns content production into a single terminal session. Each project keeps its characters, references, an
> L24: Same image model (`google/gemini-2.5-flash-image`), one shot each. The difference is the prompt path: direct prompt

## 星数曲线

```mermaid
xychart-beta
    title "eight-acres-lab/openmelon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-31 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d4f77a0d3fd1` · [字段定义](../../DATASET.md)*
