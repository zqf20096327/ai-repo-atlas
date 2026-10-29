# sugurutakahashi-1234/ai-chat-md-export

⭐ 62 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/sugurutakahashi-1234/ai-chat-md-export) · [官网](https://www.npmjs.com/package/ai-chat-md-export) · 个人维护 · 中文 README

**将 ChatGPT/Claude 聊天记录离线转为 Markdown 的 CLI 工具**

面向注重隐私的用户的命令行工具：读取 ChatGPT 与 Claude 官方导出的 conversations.json，在本地离线转换为按日期命名、含时间戳与用户/助手标记的 Markdown 文件；支持日期范围过滤、关键词搜索、合并输出、JSON 格式输出与 dry-run 预览。通过 npm、Homebrew 或下载预编译二进制安装，覆盖 Windows/macOS/Linux。限制：需用户先从平台自行导出数据，链接 24 小时过期；大文件处理尚未采用流式加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地离线转换，数据不出设备
- 支持 ChatGPT 与 Claude 两种导出格式，含自动格式检测
- 日期过滤、关键词搜索、dry-run 预览与合并单文件输出
- npm / Homebrew / 预编译二进制三种分发途径

## 适用场景

- 把 ChatGPT/Claude 聊天记录归档为可搜索的 Markdown 文件
- 在对话被删除前保留永久文本记录
- 用 grep、版本控制或笔记软件处理导出的对话

## 场景标签

 · 领域:开发者工具/数据处理

## 证据(README 行号)

> L24: `ai-chat-md-export` is a **privacy-first** CLI tool that converts ChatGPT and Claude conversations into organized, 
> L143: |`-p, --platform <platform>`|Input platform (`chatgpt`/`claude`) (required)|-|

## 星数曲线

```mermaid
xychart-beta
    title "sugurutakahashi-1234/ai-chat-md-export 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-29 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d433535aa403` · [字段定义](../../DATASET.md)*
