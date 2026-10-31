# huyang218/AiApiTest

⭐ 22 · Python · 推送 2026-03-06 · [GitHub](https://github.com/huyang218/AiApiTest) · 个人维护 · 中文 README

**检测第三方 AI API 是否提供真实原厂模型的 Web 平台**

基于 Flask 的自托管 Web 平台：向待测 API 与原厂 API 发送相同请求并对比响应相似度，判断第三方是否用低成本模型套壳冒充。检测含 8 道题的真实性验证、身份伪装与提示词泄露检测，另提供图像/视频生成模型版本检测、多模型横向对比、并发与 TTFT/TPS 性能测试及报告下载。需配置 OpenAI/Anthropic/Gemini/DeepSeek 等 9 家原厂 Key 作对比基准，支持模型名称映射；通过 start.sh、手动安装或 Docker 部署，数据存本地 SQLite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 相同请求对比原厂 API 响应相似度，判断模型真实性
- 图像/视频生成模型版本检测（4 项图像测试、端点探测）
- 并发、TTFT/TPS、Token 用量与费用预估性能测试
- 模型名称映射：第三方命名自动映射到原厂名称

## 适用场景

- 购买第三方 API 前验证是否为原厂模型
- 对比多个模型回答质量、速度与成本
- 压测 API 并发与长上下文处理能力

## 场景标签

 · 领域:LLM 基础设施/评测工具

## 证据(README 行号)

> L12: **EchoMind AI API 检测平台** 帮你一键验证，通过向待测 API 和原厂 API 发送相同请求、对比响应相似度，科学判断模型真实性。
> L19: - **真实性验证** — 8道专业题对比原厂API响应，判断是否"套壳"

## 星数曲线

```mermaid
xychart-beta
    title "huyang218/AiApiTest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4b38ea49dd7e` · [字段定义](../../DATASET.md)*
