# szilarddoro/allein

⭐ 21 · TypeScript · NOASSERTION · 推送 2026-03-15 · [GitHub](https://github.com/szilarddoro/allein) · 个人维护

**本地离线 LLM 驱动的 Markdown 编辑器**

基于 Tauri（Node.js/pnpm/Rust，用 mise 管理工具链）的 Markdown 编辑器：提供上下文感知的自动补全与拼写语法等写作改进，全部推理通过本机 Ollama 完成，写作内容不出本机，无需注册账号。应用内置 onboarding 引导下载配置模型，也可用 ollama pull 命令拉取推荐模型（qwen2.5-coder:3b-base、gemma3）后在设置中配置。开发与构建通过 pnpm tauri 命令运行，需从源码 clone 构建，无预编译安装包说明。许可证为 AGPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上下文感知的自动补全与写作改进（拼写、语法等）
- 100% 离线运行，写作内容不出本机
- 集成 Ollama，自动检测 localhost:11434 服务
- 应用内 onboarding 引导下载与配置模型

## 适用场景

- 离线写作 Markdown 并获得补全与文本改进建议
- 不注册账号、数据不出本机的 AI 辅助写作
- 本地 Ollama 用户寻找可直接使用的编辑器前端

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: A Markdown editor powered by your LLM. Like GitHub Copilot, but local and free. No account required.
> L9: - ⚡ **Context-aware autocompletion** - Like GitHub Copilot, but local
> L50: Allein integrates with Ollama to bring AI writing assistance directly into your editor. Everything runs locally—you

## 星数曲线

```mermaid
xychart-beta
    title "szilarddoro/allein 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4912c6822515` · [字段定义](../../DATASET.md)*
