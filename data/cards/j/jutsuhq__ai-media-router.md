# jutsuhq/ai-media-router

⭐ 4 · Rust · MIT · 推送 2026-11-19 · [GitHub](https://github.com/jutsuhq/ai-media-router) · [官网](https://jutsustudio.com/ai-media-router/) · 组织维护

**给 MCP 客户端用的视频/图像生成路由：40+ 供应商、比价与本地素材库**

一个 Rust 编写的 MCP 服务器，让 Claude、Cursor、Codex 等 MCP 客户端通过统一的 generate→get_job 工具调用，经 44 个内置供应商 TOML 规格（fal、Replicate、kie、Runware、BytePlus、自托管 ComfyUI 等）生成图像与视频。生成前用 search_prices 展示各供应商价格与预算校验，结果下载为本地文件并建库：全文与相似检索、引用管理（{{ref:name}}）、lineage 谱系、JSON 溯源写入媒体元数据。密钥由用户自备，存于 OS keychain 或配置文件；另提供 CLI 与 HTTP serve 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 44 个内置供应商 TOML 规格，统一 generate→get_job 工具循环
- 生成前价格目录比较与预算拒绝机制
- 本地素材库：内容哈希、全文/相似检索、lineage 谱系
- 生成文件内嵌 JSON 溯源记录（provider/model/input/parents）

## 适用场景

- 让 Claude Code 或 Cursor 里的 agent 按预算比价生成视频和图片
- 用引用管理保持角色/产品在多镜头生成中一致
- 自托管 ComfyUI 作为免费后端纳入统一调用
- 本地留存并检索所有生成资产及其来源谱系

## 场景标签

`图像生成` `视频生成` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: AI Media Router is an open-source MCP server that lets Claude, Cursor, Codex or any MCP client generate images and 
> L38: |Inference platforms and API aggregators|fal.ai (`fal`), Replicate (`replicate`), Runware (`runware`), WaveSpeedAI 
> L54: AI Media Router is not a hosted gateway like OpenRouter: there is no account, no balance and no markup, and OpenRou

## 星数曲线

```mermaid
xychart-beta
    title "jutsuhq/ai-media-router 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-02 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `de2b79f99a53` · [字段定义](../../DATASET.md)*
