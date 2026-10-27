# Hainrixz/whatsapp-closer-agentkit

⭐ 39 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/Hainrixz/whatsapp-closer-agentkit) · [官网](https://hainrixz.github.io/whatsapp-closer-agentkit/) · 个人维护 · 中文 README

**WhatsApp 销售闭环 Agent 的 Claude Code 构建蓝图（非可运行应用）**

仓库内容不是应用代码，而是 16 个分阶段 blueprint 文件、JSON Schema 合同、测试套件与审计脚本：克隆后用 Claude Code 运行 /start，由 Claude 在本地按蓝图逐阶段写出代码。目标 agent 覆盖六步流程：接收并转录音频（Whisper）、意图识别与线索资格判定、按 playbook 回复异议、Google Calendar 约日程、写入 Supabase CRM、必要时转人工；默认 borrador 模式下写操作需人工确认。支持 Meta Cloud API 与 Zernio 两种 WhatsApp 通道及免凭证 demo 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个分阶段 blueprint 文件由 Claude Code 在本地生成代码，仓库本身不含可运行代码
- 六步流程：转录、资格判定、异议回复、日程、CRM 写入、转人工
- 默认 borrador 模式：发消息/建日程/写 CRM 均需显式确认
- scripts/auditar.py 提供 23 项离线机械检查（pass/fail/parcial 三种判定）

## 适用场景

- 让 Claude Code 在我的机器上按蓝图搭建 WhatsApp 销售 agent
- 销售对话自动资格判定、异议回复与日程预约
- 构建后用审计脚本在发布前做机械检查

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L16: **Adentro no hay código que corras.** No hay `agente/`, no hay servidor, no hay `pip install`
> L24: Lo que se envía son instrucciones, contratos, pruebas y una compuerta. Se clona, se abre Claude
> L25: Code adentro de la carpeta, y se corre `/start`. Claude lee el blueprint fase por fase y
> L63: 1 · Recibí el mensaje y traé el contexto

## 星数曲线

```mermaid
xychart-beta
    title "Hainrixz/whatsapp-closer-agentkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 40
    line [38, 39]
```

2026-10-18 38 → 2026-10-27 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `f65809798e72` · [字段定义](../../DATASET.md)*
