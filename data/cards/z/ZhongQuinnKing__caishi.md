# ZhongQuinnKing/caishi

⭐ 4 · Python · NOASSERTION · 推送 2026-11-11 · [GitHub](https://github.com/ZhongQuinnKing/caishi) · 个人维护 · 中文 README

**给 AI Agent 的中文互联网读取能力包：一条命令读 33+ 站点**

以命令行与 MCP 服务器两种形式提供，让能跑命令行的 Agent 读取抖音、小红书、B站、公众号、知乎、微博、头条等中文平台内容，覆盖搜索、详情、评论、字幕、导出 Markdown 等操作，另含 dbLP 学术检索、乐谱站与任意网页正文读取。核心机制是复用用户浏览器已登录会话，只读、单条、不批量。深度读取需命令行环境，纯对话环境（如豆包）走技能的无命令路径。部分 OCR 工具需另装 tesseract 与 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令读取 33 个站点（满配 40），含抖音/B站/小红书/公众号/知乎等
- 复用用户浏览器登录会话，只读、不爬虫、不批量
- 独立包 caishi-mcp 提供自包含 MCP 服务器，接入 Claude Desktop/Cursor 等客户端
- 附带本地 OCR 小工具（zhsee/zhtable/zhslice），图片视频不出本机

## 适用场景

- 让 Claude Code 帮我读一条抖音视频的文案和评论
- 在小红书搜索内容并整理给 AI
- 把公众号文章导出成 Markdown 存档
- 对长截图和表格图片做本地文字识别

## 场景标签

`网页抓取` `OCR` · 领域:效率与自动化

## 证据(README 行号)

> L9: > **English TL;DR** — A capability pack that lets AI agents read the Chinese internet:
> L20: 一条命令读内容。给 Claude Code 这类能跑命令行的 Agent 直接用。
> L50: 不只有命令行的 AI 能用——独立包 `caishi-mcp` 是**自包含 MCP 服务器**（协议层

## 星数曲线

```mermaid
xychart-beta
    title "ZhongQuinnKing/caishi 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-20", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-02 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `eeea65318427` · [字段定义](../../DATASET.md)*
