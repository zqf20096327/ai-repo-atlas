# ECG-Rudy-Glt/PATRIMOINE

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/ECG-Rudy-Glt/PATRIMOINE) · [官网](https://patrimoine-open.gault-rudy.com) · 个人维护

**家庭自托管财富追踪器，带 AI 邮件理财建议**

面向家庭的自托管财富管理应用：通过 Enable Banking 聚合银行账户、按发薪周期做预算、追踪储蓄目标与资产配置、生成月度邮件摘要与 Excel 报表，并附带引用来源的 AI 顾问。关键机制是确定性服务负责所有数字计算，LLM 仅解读与表述，每次引用由服务器校验，估算标注 ≈。部署用 Docker Compose 两步安装，当前使用 Anthropic Claude，其他在线/本地模型接入进行中；无内置认证，需置于反向代理之后。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 Enable Banking DSP2 API 聚合全家银行账户（只读）
- AI 顾问引用的所有数字经服务器校验，计算由确定性服务完成
- 月度邮件摘要与 Excel 报表，支持 ntfy/Home Assistant 告警
- Docker Compose 部署，数据完全自托管

## 适用场景

- 把家庭所有账户、储蓄与投资集中在一处自托管查看
- 按发薪周期做预算并追踪储蓄目标达成情况
- 每月收到 AI 生成的家庭财务建议邮件

## 场景标签

 · 领域:个人/家庭理财

## 证据(README 行号)

> L3: **Tout votre patrimoine, chez vous, dans une seule interface.** Comptes, épargne, placements, budget et objectifs d'
> L49: |**Conseiller IA**|Faits chiffrés → recommandations validées. Chaque citation est vérifiée par le serveur. Aujourd'
> L54: Principe directeur : **le LLM n'invente aucun chiffre**. Les calculs sont faits par des services déterministes ; l'

## 星数曲线

```mermaid
xychart-beta
    title "ECG-Rudy-Glt/PATRIMOINE 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `746dd2ed4b94` · [字段定义](../../DATASET.md)*
