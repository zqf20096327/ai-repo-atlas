# math89423-star/AI-Academic-Polisher

⭐ 14 · Python · MIT · 推送 2026-04-28 · [GitHub](https://github.com/math89423-star/AI-Academic-Polisher) · 个人维护 · 中文 README

**学术论文 AI 润色系统：文本流式与 Word/PDF 并发润色**

面向学术写作的 AI 润色应用：支持纯文本 SSE 流式输出与 Word/PDF 段落级并发润色并保留排版，内置标准/深度改写等多套提示词策略，Markdown 热插拔。双模式部署：Server 模式用 Docker Compose（MySQL+Redis+Nginx），Desktop 模式打包为 Windows 单 EXE（SQLite+内存队列）。AI 后端走 OpenAI 兼容 API（官方/代理/Ollama），带用户与 API 线路管理后台。README 附 AIGC 检测平台测试数据与学术诚信免责声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Word/PDF 段落级并发润色并保留原始排版
- 多套润色策略提示词 Markdown 热插拔
- Docker 服务器与 Windows EXE 桌面双模式部署
- RQ 任务队列 + ThreadPoolExecutor 并发切片处理

## 适用场景

- 我把论文的 Word/PDF 文档整体提交做语言润色
- 团队在 Linux 服务器上多人共用润色服务
- 本地 Windows 上单机运行，无需配置数据库

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: 专为学术论文打磨而生的 AI 润色系统。支持纯文本流式输出和 Word/PDF 文档一键并发润色，内置多套润色风格策略，提示词热插拔配置。
> L148: |AI|OpenAI 兼容 API（官方 / 代理 / Ollama）|同左|

## 星数曲线

```mermaid
xychart-beta
    title "math89423-star/AI-Academic-Polisher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8b8994b659a0` · [字段定义](../../DATASET.md)*
