# AnnaVi11arrea1/job_seeker

⭐ 80 · JavaScript · 推送 2026-07-12 · [GitHub](https://github.com/AnnaVi11arrea1/job_seeker) · 个人维护

**本地 AI 帮求职者跟踪与按简历匹配排序职位的 Chrome 扩展**

Chrome 浏览器扩展（Manifest V3），用于求职过程管理：手动添加职位、右键保存任意网页上的职位列表、增删与浏览职位清单；可选接入本地运行的 Ollama（llama3.2，localhost:11434）读取用户简历文本，为每个职位给出 1–5 星匹配评分并按契合度排序。数据存于浏览器本地存储，无云端依赖、不联网发送数据；卸载扩展会清除已保存职位。面向个人求职者，通过开发者模式加载未打包文件夹安装，无需构建步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 右键任意网页保存职位列表
- Ollama 本地模型读取简历并给出 1–5 星匹配评分与排序
- 数据仅存浏览器本地存储，无云端依赖与账号
- Vanilla JavaScript，无框架无构建步骤

## 适用场景

- 浏览网页时随手保存各处的职位列表
- 用本地 AI 按简历契合度给职位打分排序
- 在浏览器内维护一份轻量求职跟踪清单

## 场景标签

 · 领域:求职/浏览器工具

## 证据(README 行号)

> L18: you browse, right‑click any listing out in the wild to save it, and (optionally) let a
> L29: - **🤖 AI résumé matching (optional)** — install Ollama locally, upload your résumé text, and the extension will:

## 星数曲线

```mermaid
xychart-beta
    title "AnnaVi11arrea1/job_seeker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 79 --> 81
    line [80, 80]
```

2026-10-18 80 → 2026-10-29 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1dce635b2d8d` · [字段定义](../../DATASET.md)*
