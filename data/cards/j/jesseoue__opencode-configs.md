# jesseoue/opencode-configs

⭐ 30 · Shell · 推送 2026-09-18 · [GitHub](https://github.com/jesseoue/opencode-configs) · [官网](https://openrouter.ai) · 个人维护

**OpenCode AI 编码代理的配置即代码固化栈**

面向 OpenCode CLI 与 oh-my-openagent（OmO）插件的配置仓库：通过单一 OPENROUTER_API_KEY 接入 12 个 OpenRouter 模型（GLM/DeepSeek/Gemini/Qwen/Kimi 等）加 3 个 Venice DeepSeek 通道，定义多 agent 团队（sisyphus 等 9 个主 agent、8 个子 agent、7 个团队规格）、按 agent 的模型回退、熔断器、部署前检查（oc deploy check）、低额度隔离模式与默认关闭遥测。以 git clone + oc CLI 安装，提供 oc doctor/heal/validate 等自检自修命令，仅面向 macOS 路径布局（/Users/Shared）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 OpenRouter key 接入 12 个模型，另设 Venice 内容感知通道与可选原生 DeepSeek
- 多 agent 编排：sisyphus 主导 + 8 子 agent + 7 个 tmux 团队规格
- 熔断器、按 agent 回退、部署前检查与低额度自动切换便宜模型
- oc validate/fix/heal 自修复命令与签名指纹校验，遥测默认关闭

## 适用场景

- 为 OpenCode 终端编码代理配置多模型多 agent 工作流
- 控制 LLM 使用成本并在额度不足时自动降级
- 以配置仓库方式固化 AI 编码环境，避免漂移

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L6:     ╰───╯     Pinned stack for OpenCode · OpenRouter · OmO
> L9: > **Pinned, hardened config-as-code stack for OpenCode + OpenRouter + oh-my-openagent (OmO).** OpenRouter general ga
> L41: |**OpenRouter general gateway**|GLM, DeepSeek, Gemini, MiniMax, Qwen, Kimi via one `OPENROUTER_API_KEY` — no direct

## 星数曲线

```mermaid
xychart-beta
    title "jesseoue/opencode-configs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5e0efc9c607d` · [字段定义](../../DATASET.md)*
