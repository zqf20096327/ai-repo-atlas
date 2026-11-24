# roni-clei-santos/ai-company-prospector

⭐ — · [GitHub]() · 个人维护

**Claude Code agent：按技术栈找公司并起草求职触达消息**

面向求职者的 Claude Code agent 项目：从公开来源搜索使用你技术栈的公司并生成带证据链接的 Excel 名单，按每轮 10 家处理，提取招聘人员/HR 邮箱，起草 LinkedIn 与邮件内容供人工审核后发送。三种使用路径：claude.ai 网页模式（免费账号即可）、仅生成名单模式、配合 Chrome 扩展 Claude in Chrome 的完整流程。以 skills 形式安装到 ~/.claude/skills，安装脚本处理 Python 与 RTK。设计上所有外发均为草稿，LinkedIn 仅读取；macOS 流程经作者验证，Linux/Windows 完整流程尚未经用户验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /build-company-list 从公开来源生成带证据与链接的公司名单 Excel
- /next-companies 每轮处理 10 家并在轮次间保留进度记忆（progresso.json）
- 起草的 LinkedIn/邮件均需人工审核，LinkedIn 操作仅限只读
- 提供网页模式：免费 claude.ai 账号粘贴文本即可获得名单

## 适用场景

- 按自己掌握的技术栈筛选目标公司并逐家触达
- 批量准备个性化的 LinkedIn 与邮件求职草稿
- 不安装任何东西，用 claude.ai 网页版先试跑公司名单

## 场景标签

 · 领域:求职/销售触达自动化

## 证据(README 行号)

> L5:  Um agente para o Claude Code que monta a lista de empresas que usam a sua tecnologia, investiga uma por uma
> L46:  Lista de empresas com fonte O <code>/build-company-list</code> monta a planilha a partir de fontes públicas, com e
> L113: Depois, nos três sistemas: preencha o `perfil.local.md`, abra o Claude Code na pasta (`claude`) e rode **`/build-c

## 星数曲线

```mermaid
xychart-beta
    title "roni-clei-santos/ai-company-prospector 星数(近 2 点)"
    x-axis ["2026-11-12", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-12 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0fac93f94082` · [字段定义](../../DATASET.md)*
