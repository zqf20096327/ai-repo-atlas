# Ayanlin1688/Minimax-H3-Tiktok-skill

⭐ 3 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/Ayanlin1688/Minimax-H3-Tiktok-skill) · 个人维护

**给跨境电商卖家生成 TikTok 美区带货视频提示词的 Skill**

一套面向 MiniMax H3（海螺 02）视频模型的提示词工程规范，以 SKILL.md 与模板文件形式发布。用户上传产品图后，Skill 按 27 条铁律、36 项自检和 T×C×S 三层路由（尺寸档位×品类语法×监管合规）生成可直接粘贴进海螺 AI 的带货视频提示词。规则由逐帧分析翻车视频逆向整理而来，并与 MiniMax H3 官方规范做了对齐审计。安装方式为 clone 仓库后在对话中引用路径，或放入客户端 skills 目录。能力边界部分声明无法保证每条视频完美。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 27 条铁律 + 36 项自检的提示词规范，覆盖多手/悬空/穿模/蜡像脸等反缺陷项
- T（尺寸）× C（品类）× S（监管）三层路由，全类目商品落位
- 提供全类目通用主模板与真实感六问验收流程
- 与 MiniMax H3 官方规范对齐，自动审计 11/11 通过

## 适用场景

- 为 TikTok Shop 美区商品批量生成 15 秒带货视频提示词
- 规避 AI 生成带货视频中的手部、穿模与蜡像脸缺陷
- 保健品/医疗器械/儿童母婴等受监管品类提示词的合规措辞

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: 一套给 **MiniMax H3 视频模型**用的提示词工程规范。
> L191: ├── SKILL.md                              ★ 核心规范：27 条铁律 + 36 项自检
> L292: Built by reverse-engineering **five rounds of failed AI videos frame by frame**. It combines a **positive realism 

## 星数曲线

```mermaid
xychart-beta
    title "Ayanlin1688/Minimax-H3-Tiktok-skill 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `831db40baef0` · [字段定义](../../DATASET.md)*
