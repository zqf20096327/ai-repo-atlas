# Dradradre/korean-anti-slop-writing

⭐ 3 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/Dradradre/korean-anti-slop-writing) · 个人维护

**检测并改写韩语文本中 AI 腔调的 Claude Code/Codex 技能**

面向韩语写作的去 AI 化工具：以 Claude Code 与 Codex 技能形式提供，内置 66 条检测规则与 21 条改写规则、58 项核对清单，检出 AI 常见句式（套路语、翻译腔、模型口头禅、提示词副作用等）并改写为自然表达。检测脚本仅用 Python 3 标准库，可脱离 agent 单独运行，支持报告/对话/UI 三种文体模式与 JSON 输出；安装方式为 git clone 到技能目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 66 条检测规则覆盖标点、结构信号、模型口头禅、提示词副作用等类别
- 仅依赖 Python 3 标准库，无额外包安装
- 支持 report/chat/ui 三种文体模式与 --json 输出
- 可作为 Claude Code/Codex 技能运行，检测脚本也可单独执行

## 适用场景

- 改写报告和邮件里的 AI 腔调
- 检查博客文章是否有 AI 痕迹
- 处理客服消息与界面文案的语气

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L1: AI 티 빼기. 한국어 글에 남은 AI 말투를 찾아서 고칩니다.
> L10: 보고서, 업무 메일, 고객 메신저 회신, 화면 문구, 탐지 룰 설명, 블로그 글을 다룹니다. Claude Code와 Codex에서 스킬로 씁니다. 검사 스크립트만 따로 돌려도 됩니다.
> L39: python scripts/lint_korean_slop.py 보고서.md

## 星数曲线

```mermaid
xychart-beta
    title "Dradradre/korean-anti-slop-writing 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `98e1ad2ff882` · [字段定义](../../DATASET.md)*
