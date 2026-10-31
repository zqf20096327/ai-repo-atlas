# frangelbarrera/Network-Scanner

⭐ 24 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/frangelbarrera/Network-Scanner) · 个人维护

**AI 辅助的网络侦察与安全评估工具包（CLI/Web/API/PDF 报告）**

开源安全评估工具包，结合 DNS、WHOIS、子域名枚举、端口扫描与部分 Web 检查，以 Python Flask 后端与 React 前端提供 CLI、Web 界面、REST API 与 HTML/PDF 报告。AI 部分为可选的 OpenAI 聊天助手：解读扫描结果、风险分级建议与修复建议，输出为参考性质需人工验证，配置后消息与扫描结果会发送至 OpenAI。面向安全研究、教学实验与明确授权的评估场景，支持 docker-compose 部署与令牌保护的生产配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 子域名/端口/DNS/WHOIS 五类扫描与组合扫描工作流
- OpenAI 驱动的可选 AI 助手：结果解读、优先级与修复建议
- CLI、Web 界面、REST API（令牌保护与限流）三种使用方式
- HTML/PDF/JSON 报告生成与 docker-compose 部署

## 适用场景

- 对自有或已授权系统做子域名、端口与漏洞启发式检查
- 生成面向干系人的安全扫描报告
- 借助 AI 助手与 Learning Mode 学习安全概念

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: Network Scanner is an open-source toolkit that combines DNS, WHOIS, subdomain, port and selected web checks with a C
> L68: The project intentionally combines stable workflows with experimental checks. DNS and WHOIS lookups, subdomain reco
> L178: - **AI Assistant**: Optional OpenAI integration for assisted analysis and recommendations; when configured, submit

## 星数曲线

```mermaid
xychart-beta
    title "frangelbarrera/Network-Scanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4b983dc27449` · [字段定义](../../DATASET.md)*
