# huggingface/safeagents

⭐ 419 · Python · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/huggingface/safeagents) · 组织维护

**给 coding agent 加本地安全代理：拦截工具调用并脱敏轨迹**

位于 agent 与模型服务器之间的轻量本地代理：在 harness 执行前检查模型发起的每次工具调用，被拦截的调用替换为文本提示。检查分三层——请求声明校验、atif-scan 检测器、可选 judge 决策模型；支持任何可设 base URL 的 harness，覆盖 OpenAI Chat Completions 与 Anthropic Messages 协议，流式与非流式均可。另提供轨迹脱敏（scrub）、发布到 HF 数据集（publish）、judge 模型基准榜与运行监控界面。脚本安装，Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层工具调用检查：请求校验、atif-scan 检测器、可选 judge 模型
- 兼容任意可设 base URL 的 harness（Claude Code、OpenCode 等 13 个提供配置指南）
- safeagents scrub 识别凭据、邮箱、家目录等并脱敏 agent 轨迹
- 插件机制支持本地 Python 或 Hugging Face Hub 加载

## 适用场景

- 运行 coding agent 时拦截危险工具调用
- 发布 agent 轨迹数据集前自动清除凭据与隐私信息
- 为 agent 选 judge 决策模型时参考 judge-bench 排行榜

## 场景标签

`编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L3: A lightweight local proxy between your agent and its model server. It checks every tool call the model makes before 
> L43: ## How it works
> L45: Each tool call goes through three stages:

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/safeagents 星数(近 18 点)"
    x-axis ["2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 0 --> 458
    line [25, 47, 54, 59, 118, 144, 148, 149, 151, 248, 306, 338, 378, 394, 404, 409, 414, 419]
```

2026-10-30 25 → 2026-11-25 419（+394）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `f633ff296483` · [字段定义](../../DATASET.md)*
