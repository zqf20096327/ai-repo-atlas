# yoli-mi/good-learning

⭐ 350 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/yoli-mi/good-learning) · 个人维护 · 中文 README

**为 AI agent 提供学习计划、错题复盘与 LaTeX PDF 生成能力的 skill**

一个面向 AI agent（以 Codex 为例）的学习与备考 skill：根据考纲、教材、真题和可用时间生成知识清单、备考计划与每日课程，并依据用户真实作答制作错题本、调整后续安排。配套 Python 脚本负责 Markdown 转 LaTeX 并经 XeLaTeX/LuaLaTeX 编译为 PDF，以及从 JSON 生成 SVG/PNG 总结思维导图。仓库只含 skill 指令与生成脚本，不含教材或试卷等内容，安装方式为克隆到 agent 的 skills 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识清单与备考计划分离生成，保留知识点编号、验收标准及来源
- 错题本依据真实作答生成，演示错误单独标记不计入掌握状态
- 当日复盘输出 SVG 思维导图，可选生成 PNG（需中文字体）
- 课程、清单、计划、错题本均可编译为 PDF，源文件归档到源文件子目录

## 适用场景

- 结合考纲和每日可用时间制定结构化备考计划
- 零基础或复习模式下按日生成含例题与变式练习的课程
- 提交作答后自动整理错题本并更新后续学习安排

## 场景标签

 · 领域:教育/学习工具

## 证据(README 行号)

> L3: 一个用于 AI agent 的学习与备考 skill：根据考纲、教材、真题和可用时间建立知识清单、备考计划与每日课程，再依据真实作答整理错题并调整后续安排
> L26: 以codex为示例：把仓库克隆或复制为 Codex skills 目录下的 `good-learning` 文件夹，重启 Codex 或重新加载 skills 后即可使用


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `f2a111d1cd8b` · [字段定义](../../DATASET.md)*
