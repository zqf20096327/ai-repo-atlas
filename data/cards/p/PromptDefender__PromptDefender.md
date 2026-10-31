# PromptDefender/PromptDefender

⭐ 22 · Go · Apache-2.0 · 推送 2026-04-08 · [GitHub](https://github.com/PromptDefender/PromptDefender) · [官网](https://promptshield.readme.io) · 组织维护

**多层提示注入防护服务：输入清洗、提示包裹与响应校验**

面向 LLM 应用的提示注入防御项目，由多层防线组成：Wall 层对输入做清洗与规则检查（越狱关键词、PII 识别、攻击者标识探测）；Keep 层在提示中包裹指令防御（如提醒不泄露密钥）；Drawbridge 校验 LLM 响应（金丝雀检测、脚本清理），README 标注 Coming soon。以 Terraform 部署的服务形式提供，含托管版本与开发者门户 API，通过 make 命令部署与运行集成测试，依赖 URL 与 DEFENDER_API_KEY 环境变量。

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

- Wall 输入清洗：越狱关键词、PII 识别、攻击探测
- Keep 提示包裹式指令防御
- Drawbridge 响应校验：金丝雀检测与脚本清理（Coming soon）
- Terraform 一键部署 + make 集成测试与 k6 负载测试

## 适用场景

- 为接入任意 LLM API 的应用加提示注入防护
- 防止用户输入把 PII 泄露给 LLM
- 校验 LLM 输出中是否泄露密钥或含脚本

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L16: A prompt defence is a multi-layer defence that can be used to protect your applications against prompt injection
> L33: Keep is a layer of defence on the prompt itself - it effectively wraps your prompt in an effective 'prompt defence'

## 星数曲线

```mermaid
xychart-beta
    title "PromptDefender/PromptDefender 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b08e4f90a4a8` · [字段定义](../../DATASET.md)*
