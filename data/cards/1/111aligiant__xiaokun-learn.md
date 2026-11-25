# 111aligiant/xiaokun-learn

⭐ 4 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/111aligiant/xiaokun-learn) · [官网](https://111aligiant.github.io/xiaokun-learn/) · 个人维护 · 中文 README

**手机上的 AI 编程私教：本地真跑 Python/SQLite 的开源教学模板**

面向手机端的开源 AI 编程学习应用，提供 Python 与 SQLite 各 17 节课程。代码经 Pyodide（CPython/WASM）与 sql.js（SQLite/WASM）在设备本地执行，无后端、离线优先，学习数据与 API Key 只存本机。助教对话接入任意 OpenAI 兼容平台（自带 Key），并按学员画像实时改写课程例子与练习。人设、画像字段、课程包均为可替换的 JS 数据，同一套代码可发布为 PWA 或 Android APK（需 JDK 21 与 Android SDK 打包）。界面目前仅简体中文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pyodide 与 sql.js 在设备本地执行 Python/SQLite 代码，不经服务器
- 任意 OpenAI 兼容平台接入，Key/base_url/模型名可自由填写，预设快捷填充
- 学员画像实时改写课程正文、练习题与实操台演示数据
- 人设、画像、课程包为普通 JS 数据，可 fork 改成其他学科

## 适用场景

- 自学编程的人在手机上跟路线学 Python/SQLite，卡住随时问助教
- 家长或老师为学生配置会记住基础与目标的专属助教
- AI 教育产品开发者 fork 模板改成其他学科的讲解-练习-反馈应用
- 断网或不想上传代码的环境下在手机上跑代码做练习

## 场景标签

`教程课程` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5:  手机上的 AI 编程私教。代码在手机上真跑，模型用你自己的 Key，课程和人设可以整个换掉。
> L36: |怎么跑代码|Pyodide（CPython/WASM）+ sql.js（SQLite/WASM），不经过服务器|
> L58: - Python 用 **Pyodide**（CPython/WASM），SQL 用 **sql.js**（SQLite/WASM），不需要服务器
> L74: - 支持任意 **OpenAI 兼容平台**：DeepSeek / OpenAI / 通义千问 / 智谱 GLM / Kimi / 硅基流动，内置快捷填充

## 星数曲线

```mermaid
xychart-beta
    title "111aligiant/xiaokun-learn 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-11-08", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-28 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `cbd0d8ca6998` · [字段定义](../../DATASET.md)*
