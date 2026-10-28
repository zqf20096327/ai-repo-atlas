# rajeevbarde/SDLora-Organizer

⭐ 47 · JavaScript · MIT · 推送 2026-07-31 · [GitHub](https://github.com/rajeevbarde/SDLora-Organizer) · 个人维护

**基于预抓取 CivitAI 数据库的 LoRA 模型整理与下载应用**

面向 Stable Diffusion LoRA 使用者的本地 Web 应用：通过预抓取的 CivitAI 数据库（models_standalone.db，数据截至 2025 年 5 月 7 日）离线浏览与筛选 LoRA，按用户提供的 Civitai token 下载新模型，并支持扫描注册本地已有 LoRA、校验文件、检测重复与孤立文件、获取触发词、生成 LoRA 档案页与仪表盘。安装需 Node.js 20，README 声明面向 Windows 11（Linux 可能不可用），通过 start_servers.bat 启动后在浏览器 localhost:5173 使用；数据库文件需另行下载并配置路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描、注册并校验本地已有 LoRA 文件
- 基于预抓取数据库的筛选下载，需配置 Civitai token
- 重复与孤立 LoRA 检测，获取 LoRA 触发词
- 已注册 LoRA 的档案页与仪表盘

## 适用场景

- 整理本地散落的 LoRA 收藏并检测重复
- 离线浏览 CivitAI LoRA 数据库并按需下载
- 查看 LoRA 的触发词以便在 Stable Diffusion 中使用

## 场景标签

 · 领域:AI 模型资产管理/生成式创作工具

## 证据(README 行号)

> L17: |⬇️ **Download LoRA from Civitai with Filters**|Screenshots and Steps|
> L42: 7. Download new LoRA from CivitAI if you want.

## 星数曲线

```mermaid
xychart-beta
    title "rajeevbarde/SDLora-Organizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-28 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9cc34b0e4b40` · [字段定义](../../DATASET.md)*
