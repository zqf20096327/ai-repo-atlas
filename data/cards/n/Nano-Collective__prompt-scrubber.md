# Nano-Collective/prompt-scrubber

⭐ 23 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Nano-Collective/prompt-scrubber) · 组织维护

**本地优先的提示词脱敏工具：发送云端 LLM 前替换敏感信息**

prompt-scrub 在提示词离开本机前检测并替换邮箱、密钥、路径、URL、电话、信用卡、IBAN、SSN、IP 等识别性内容，映射为稳定占位符，并在本地将模型回复还原（rehydrate）。提供 CLI 与 Node.js API，含 inspect（检出实体表）、diff（前后对比）、置信度阈值、会话文件加密与 TTL 回收、剪贴板监听，以及可将 SDK 指向本地的透明脱敏代理（支持 OpenAI 上游与 SSE 流式）。README 明确声明这是内容层的部分防护而非匿名化，不覆盖网络层、风格指纹等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 类敏感数据本地替换为稳定占位符并支持回复本地还原
- inspect/diff/--min-confidence 让用户在发送前审查看检出结果
- 透明脱敏代理可将 SDK 流量导向本地，出站脱敏、回程还原
- 会话文件支持加密（PROMPT_SCRUB_KEY）与 TTL 自动回收

## 适用场景

- 把含个人信息的提示词脱敏后再发给云端 LLM
- 让现有 OpenAI SDK 应用无改动地经过脱敏代理
- 在发送前用 inspect 审查哪些实体被检出、哪些可能漏检

## 场景标签

 · 领域:LLM 基础设施/隐私工具

## 证据(README 行号)

> L5: `prompt-scrub` is a local-first utility designed to strip identifying content out of prompts and messages before the
> L133: prompt-scrub proxy --target https://api.openai.com --port 8080 &

## 星数曲线

```mermaid
xychart-beta
    title "Nano-Collective/prompt-scrubber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `14d80aee6b37` · [字段定义](../../DATASET.md)*
