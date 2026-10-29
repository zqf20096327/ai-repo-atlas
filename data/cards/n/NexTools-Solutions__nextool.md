# NexTools-Solutions/nextool

⭐ 23 · PHP · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/NexTools-Solutions/nextool) · [官网](https://linkedin.com/in/richard-ti/) · 组织维护

**GLPI 10-12 模块化插件中心：按需启用运维与 AI 功能**

NexTool 是 GLPI（IT 资产与服务台系统）的插件枢纽，同一安装包兼容 GLPI 10/11/12，从统一界面按需安装模块。免费模块含 AI Assist（工单摘要、回复建议、情感分析、自动分类，支持自带 OpenAI/Gemini/Anthropic key 或托管模式）、条码标签、CVE 扫描、Telegram/WhatsApp 通知等；另有约 20 个付费许可模块（电子签名、SSO、库存管理等）。要求 PHP 扩展 curl/phar/zip 与 sodium 或 openssl 3.0+，安装提供自动脚本（含 SHA256 校验）或 GLPI 标准手动方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一安装包兼容 GLPI 10/11/12
- AI Assist 模块支持 OpenAI/Gemini/Anthropic 自带 key 或托管模式
- 约 16 个免费模块与 20 个许可模块按需启用
- install.sh 自动脚本含 SHA256 完整性校验

## 适用场景

- 在 GLPI 中给工单接入 AI 摘要与回复建议
- 统一管理 GLPI 的标签、安全扫描、通知等增强功能
- 通过 WhatsApp/Telegram 通知与交互处理工单

## 场景标签

`AI 助手` `网络安全` · 领域:对话与助手

## 证据(README 行号)

> L3: O **NexTool Solutions** é um hub de soluções dentro do GLPI: você habilita apenas o que precisa e mantém tudo centra
> L35: - **AI Assist** \
> L36:  Descrição: IA no chamado e na base de conhecimento – resumo, sugestão de resposta, análise de sentimento, triagem 

## 星数曲线

```mermaid
xychart-beta
    title "NexTools-Solutions/nextool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ba3e18a8a979` · [字段定义](../../DATASET.md)*
