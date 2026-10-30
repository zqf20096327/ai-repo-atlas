# openapi/openapi-skills

⭐ 15 · Shell · MIT · 推送 2026-09-15 · [GitHub](https://github.com/openapi/openapi-skills) · [官网](https://openapi.com) · 组织维护

**Openapi API 市场的 agent 技能集：公司数据/KYC/电子签等 12 个领域**

由 Openapi 公司维护的 agent 技能仓库：提供 12 个按领域划分的 SKILL.md 格式技能，覆盖 OAuth 认证、公司数据查询、官方文件、征信/KYC、电子签名（eIDAS）、电子发票、短信/PEC、地理编码与车辆数据等，供 Claude Code 及任何兼容 SKILL.md 的 agent 调用 Openapi API 市场。仓库将 knowledge/（构建期维护材料）与 skills/（自包含交付物）严格分离；技能需要 OPENAPI_EMAIL/OPENAPI_API_KEY 或 Bearer token 环境变量。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个领域技能（认证/公司数据/KYC/电子签名/电子发票/SMS/PEC 等）
- knowledge/ 与 skills/ 分离，SKILL.md 自包含、不依赖仓库内部知识
- 兼容 Claude Code 及任何 SKILL.md 兼容 agent
- 通过 npx skills add 一条命令安装

## 适用场景

- 让 Claude Code 等 agent 直接调用 Openapi API 市场的服务
- 开发涉及意大利/EU 企业数据、KYC、电子签名的自动化流程
- agent 内完成电子发票开具与短信/PEC 发送

## 场景标签

 · 领域:开发者工具/API 集成

## 证据(README 行号)

> L17:  Agent skills to interact with Openapi® APIs from Claude Code and any SKILL.md-compatible agent
> L27: Agent skills for using and integrating the services of the Openapi API marketplace — the largest certified API mark

## 星数曲线

```mermaid
xychart-beta
    title "openapi/openapi-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `53216c71360f` · [字段定义](../../DATASET.md)*
