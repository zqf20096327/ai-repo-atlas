# rcngo/fluxo-nfs-e-automatico-brasil

⭐ 3 · JavaScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/rcngo/fluxo-nfs-e-automatico-brasil) · 个人维护

**巴西会计事务所的自动开具 NFS-e 服务发票系统**

面向巴西会计事务所的应用：客户通过 e-mail 或 WhatsApp 提出开票请求，AI 负责读取并提取请求中的信息（CNPJ、金额、月份等），是否开票、追问还是转人工由代码中的固定规则决定，开票通过 NFE.io 完成，税额（ISS）由 NFE.io 按企业配置计算。应用本身不计算税额，拿不准时追问、无法处理时转给事务所员工。员工通过浏览器面板管理请求、已开发票、转办与配置；支持每日自动备份并做恢复验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 只读取请求，开票/追问/转人工由经测试的确定性代码规则决定
- 三条处理路径：数据齐全即开票（附 PDF/XML）、信息缺失则追问、疑难转人工
- 默认仅在 NFE.io 测试环境开票，真实开票需事务所正式决定
- 提供生产服务器安装脚本、每日自动备份（含恢复测试）与运行手册

## 适用场景

- 会计事务所客户通过 WhatsApp/邮件请求服务发票并自动获得 PDF/XML
- 让系统先在 NFE.io 测试环境试运行，再由事务所决定开启真实开票
- 通过面板统一管理客户企业、服务目录与可开票人员

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Os clientes do escritório pedem a nota fiscal de serviço por **e-mail** ou **WhatsApp**, do jeito que já pedem hoje 
> L17: - **A IA só lê o pedido.** Quem decide se emite, pergunta ou encaminha são regras fixas no código, testadas uma a u
> L33: |**motor**|o programa principal (Node.js): as regras, a conversa com a IA e com a NFE.io, e o painel|

## 星数曲线

```mermaid
xychart-beta
    title "rcngo/fluxo-nfs-e-automatico-brasil 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-22 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `2e972a1ea66c` · [字段定义](../../DATASET.md)*
