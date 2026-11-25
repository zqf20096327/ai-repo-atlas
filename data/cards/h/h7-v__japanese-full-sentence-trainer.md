# h7-v/japanese-full-sentence-trainer

⭐ 10 · JavaScript · 推送 2026-07-09 · [GitHub](https://github.com/h7-v/japanese-full-sentence-trainer) · 个人维护

**日语全句翻译练习应用：用 LLM 为学习者批改答案**

本地运行的全句翻译练习应用：显示英文句子、要求输入日语翻译，并由 LLM 将答案判定为正确、接近或错误。句子来源支持 Anki（经 AnkiConnect 只读取）、Bunpro 非官方前端 API 与 CSV（上限 5000 行），并内置 10 句 N5 演示句。提供打包版下载，无需 Node.js/npm/Git；API key 与 token 保存于本地 .env。托管 LLM 需自备 key 并计费，本地 OpenAI 兼容服务器可避免数据外发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 批改全句翻译，反馈分正确/接近/错误三档
- 支持 Anki、Bunpro、CSV 三种句子导入源及内置演示句
- 兼容本地 OpenAI 兼容服务器、OpenAI API 与 Gemini API
- 打包版含自动更新机制并保留 .env 与缓存

## 适用场景

- 练习日语句子翻译并让 AI 批改我的答案
- 把 Anki 或 Bunpro 里学过的句子导入做翻译练习
- 不想把练习内容发给托管 LLM，用本地模型批改

## 场景标签

 · 领域:语言学习工具

## 证据(README 行号)

> L3: A local practice app for full-sentence Japanese translation practice.
> L5: It shows you an English sentence, asks you to type the Japanese, and uses an LLM to grade whether your answer is cor
> L41: - An LLM API key so the app can grade answers.

## 星数曲线

```mermaid
xychart-beta
    title "h7-v/japanese-full-sentence-trainer 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `acab73cbc872` · [字段定义](../../DATASET.md)*
