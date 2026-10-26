# acheAIsuiyimen/ache-life-to-comic-skill

⭐ 78 · JavaScript · NOASSERTION · 推送 2026-08-09 · [GitHub](https://github.com/acheAIsuiyimen/ache-life-to-comic-skill) · [官网](https://ai-suiyimen-site.openai.site) · 个人维护 · 中文 README

**把日常、照片、会议与长文收进按月成册的漫画手帐 AI skill**

面向个人用户的 Claude 类 Agent 技能（SKILL.md 格式）：用户发来一句话、照片、知识笔记、会议纪要或长文，skill 自动排版为带章节封面的漫画手帐，按月装订、季度成部、年末生成合辑索引。提供五款画风预设与参考图风格拆解，排版由确定性渲染器（page-renderer.mjs 等）承担而非纯提示词；上下文只带书级设定与最近五条摘要。通过 npx skills add 安装，源码可见但限非商业使用（PolyForm Noncommercial）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一句话/照片/会议/长文多类输入自动排版为漫画章节并按月装订
- 五款画风预设，可上传参考图拆解媒介与构图
- 确定性渲染器负责页面比例、字体与装订，配 84/84 自动化回归
- 上下文只带书级设定与最近五条摘要，长期连载不线性变慢

## 适用场景

- 把日常心情和照片持续收进一本漫画手帐
- 会议纪要转成轻配图的可读页面
- 长文按原顺序排进正文主导的版面

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3:  Ache life-to-comic skill：日常、照片、知识、会议、长文和角色进入同一本书
> L61: npx skills add https://github.com/acheAIsuiyimen/ache-life-to-comic-skill --skill ache-life-to-comic-skill
> L98: 每次正式输入都有自己的章节封面。一个月的内容持续进入同一本月册，每三个月形成一部，年末再生成合辑索引。不是每章散落一个 HTML 文件，也不会因为连载一年就把全部历史塞进上下文。

## 星数曲线

```mermaid
xychart-beta
    title "acheAIsuiyimen/ache-life-to-comic-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-26 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6fcc2c681110` · [字段定义](../../DATASET.md)*
