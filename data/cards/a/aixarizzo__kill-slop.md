# aixarizzo/kill-slop

⭐ 20 · MIT · 推送 2026-08-06 · [GitHub](https://github.com/aixarizzo/kill-slop) · [官网](https://aixarizzo.com) · 个人维护

**两个 Claude Code 技能：按作者本人声音审计并修复 AI 腔文本**

由两个 Claude Code skill 组成的文本审计工具：kill-slop 是工作流，读取文件或草稿，对照作者声音逐行审计，报告每处失败行及原因与替换建议，仅应用用户批准的修改，最多执行两轮修复；anti-slop 是其加载的方法，包含 AI 特征目录、评分规则与声音绑定协议，也可在起草新文本时独立触发。方法来源包括约 18 篇 RLHF 多样性坍缩论文、Wikipedia WP:AISIGNS 目录与单一作者推文声音研究。判定基于作者真实声音而非全局禁词表，约 100 词内出现三个目录特征才标记改写；若当前会话写了草稿，审计在独立的新上下文 agent 中运行。安装方式为 git clone 后复制到 ~/.claude/skills/，需提供声音文件、5 篇以上真实写作样本或指定语域，否则技能会停止并说明。

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

- 对照作者本人声音逐行审计，报告失败原因与替换建议
- 仅应用用户批准的修改，最多两轮修复防止过度校正
- anti-slop 提供 AI 特征目录、评分规则与声音绑定协议
- 当前会话生成的草稿在独立新上下文 agent 中审计，避免自评

## 适用场景

- 把我写的草稿里的 AI 腔找出来并按我的风格改掉
- 起草新文本时自动按我的声音把关
- 审计演示文稿等材料是否像 AI 写的

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: Two Claude Code skills for finding and fixing AI-sounding text in writing that is supposed to sound like a person.
> L5: `kill-slop` is the workflow. Point it at a file or a pasted draft and it audits the text against the author's voice,

## 星数曲线

```mermaid
xychart-beta
    title "aixarizzo/kill-slop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `dd436240948b` · [字段定义](../../DATASET.md)*
