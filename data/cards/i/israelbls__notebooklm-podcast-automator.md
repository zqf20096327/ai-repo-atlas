# israelbls/notebooklm-podcast-automator

⭐ 117 · Python · MIT · 推送 2026-06-11 · [GitHub](https://github.com/israelbls/notebooklm-podcast-automator) · 个人维护

**用 API 自动化操作 Google NotebookLM 生成播客音频**

基于 FastAPI 与 Playwright 的 REST 服务，通过浏览器自动化操作 Google NotebookLM：向指定笔记本上传来源（URL、YouTube、文本），触发 Audio Overview 生成并跟踪状态、返回下载链接或音频文件。自动处理英文与希伯来语界面，可自动启动专用 Chrome 配置文件或附加到已有远程调试会话。需自备 NotebookLM 账号、Python 3.9+ 与 Chrome/Chromium；首次运行需在弹出的浏览器窗口中手动登录 Google 账号。提供 uv/pip 安装与 Docker 构建，测试套件未随仓库附带。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- REST API 上传 URL/YouTube/文本来源到笔记本
- 触发 Audio Overview 生成（可选风格与提示词覆盖）并跟踪状态、获取音频
- 自动处理英文与希伯来语 NotebookLM 界面
- Chrome 专用配置文件自动启动或附加已有远程调试会话

## 适用场景

- 批量把来源导入 NotebookLM 并生成播客式音频
- 在流水线中程序化获取 Audio Overview 音频文件
- 无人值守调用 NotebookLM 免去手动点选界面

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: Automate Google NotebookLM with a small FastAPI service and Playwright. Upload sources (URLs, YouTube videos, or raw
> L7: - Trigger Audio Overview generation with optional style and prompt overrides.

## 星数曲线

```mermaid
xychart-beta
    title "israelbls/notebooklm-podcast-automator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 115 --> 118
    line [116, 117, 117]
```

2026-10-18 116 → 2026-10-24 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7d915f05f150` · [字段定义](../../DATASET.md)*
