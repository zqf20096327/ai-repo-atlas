# melgarafael/DeskcommCRM

⭐ 5,595 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/melgarafael/DeskcommCRM) · [官网](https://deskcomm.com.br) · 个人维护

**自托管开源 CRM，AI agent 经 WhatsApp 接待、鉴定并成交客户**

基于 Next.js/TypeScript/Supabase 的自托管销售 CRM：AI agent 通过 WhatsApp（WAHA 网关）接待客户、资质鉴定并完成销售，含销售漏斗与自动化规则（cron 驱动）。安装路径为 VPS 上的 git clone + install.sh 脚本，使用预构建 Docker 镜像，无需安装 Node 或编译；支持 ARM64、自动 HTTPS、幂等重装、界面内一键更新与失败回滚。MIT 许可，多租户，定位 LGPD 合规，支持 MCP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI agent 经 WhatsApp 接待、资质鉴定并销售
- 一条命令 VPS 安装：预构建镜像，自动 HTTPS，幂等
- 界面内更新：自动备份、失败自动回滚、维护时间窗
- 多租户、MCP 就绪、LGPD 定位

## 适用场景

- 用 WhatsApp 做销售渠道的商家自托管客户管理
- 替代按月付费的聊天销售 CRM 并保留数据自主权
- 为不同垂直行业客户批量部署聊天销售系统

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: **Agentes de IA que atendem, qualificam e vendem no WhatsApp — dentro de um CRM open source rodando no seu servidor.
> L85: |**IA**|Uma chave de **OpenRouter**, **Anthropic** ou **OpenAI** — o instalador pergunta qual você quer|

## 星数曲线

```mermaid
xychart-beta
    title "melgarafael/DeskcommCRM 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 4757 --> 5671
    line [4848, 4859, 4879, 4904, 4930, 4970, 5000, 5030, 4833, 5278, 5331, 5357, 5389, 5404, 5412, 5420, 5438, 5457, 5469, 5490, 5500, 5510, 5519, 5530, 5549, 5574, 5595]
```

2026-10-26 4,848 → 2026-11-28 5,595（+747）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `3f9c19a09999` · [字段定义](../../DATASET.md)*
