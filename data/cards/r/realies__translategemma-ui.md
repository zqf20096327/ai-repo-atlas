# realies/translategemma-ui

⭐ 53 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/realies/translategemma-ui) · [官网](https://hub.docker.com/r/realies/translategemma-ui) · 个人维护

**自托管 Web 界面：通过 Ollama 本地运行 TranslateGemma 翻译模型**

为 Google 开源翻译模型 TranslateGemma 提供 Web 操作界面：支持 55 种语言的选择器、输入即译的自动翻译、语言对调换、翻译时长与 token 数统计，界面标签随浏览器语言本地化并支持明暗模式。推理通过本地 Ollama 完成，数据不离开本机；需预先运行 Ollama 并拉取 translategemma 模型（27b/12b/4b 三档，约 2.5–16GB）。以多架构 Docker 镜像（linux/amd64、linux/arm64）分发，通过环境变量配置 Ollama 地址、模型与端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 55 种语言的可搜索选择器与最近语言记录
- 输入即自动翻译，无需点击按钮
- 推理经本地 Ollama 完成，数据不离开本机
- 多架构 Docker 镜像（linux/amd64、linux/arm64）

## 适用场景

- 在本机自托管一个翻译界面，避免数据外发
- 日常多语言文本翻译，切换语言对并查看 token/耗时统计
- 用 Docker 快速部署到家庭服务器供局域网使用

## 场景标签

 · 领域:翻译/Web 应用

## 证据(README 行号)

> L7: Web interface for TranslateGemma, Google's open translation model.
> L15: - **Local inference** — no data leaves your machine, powered by Ollama

## 星数曲线

```mermaid
xychart-beta
    title "realies/translategemma-ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-28 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8e8bbedfdcd4` · [字段定义](../../DATASET.md)*
