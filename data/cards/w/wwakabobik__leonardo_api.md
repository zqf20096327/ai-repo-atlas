# wwakabobik/leonardo_api

⭐ 30 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/wwakabobik/leonardo_api) · [官网](https://pypi.org/project/leonardo-api/) · 个人维护

**Leonardo.ai 图像生成 API 的 Python 客户端库**

基于 Leonardo.ai 官方 API 文档封装的 Python 包，提供同步（requests）与异步（aiohttp）两种客户端类 `Leonardo` / `LeonardoAsync`。用户需持有 Leonardo.ai 付费订阅并生成 API 访问令牌；库支持获取用户信息、提交文生图任务（prompt、negative_prompt、模型 ID、尺寸、guidance_scale 等参数）、轮询/等待任务完成并取回图片 URL，另内置平台/社区/NSFW 模型的预载字典。通过 pip 从 PyPI 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步 requests 与异步 aiohttp 双客户端可选
- 支持文生图任务提交、等待完成与取回图片 URL 的完整流程
- 内置 platform/custom/nsfw 模型预载字典
- 需 Leonardo.ai 付费订阅的 API 访问令牌

## 适用场景

- 在 Python 项目中调用 Leonardo.ai 生成图像
- 异步场景下集成 Leonardo 图像生成服务
- 查询可用模型列表并按模型 ID 生成图片

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L10: This package contains Python API for Leonardo.ai based on official API documentation.
> L20: This Python API provides access to Leonardo API using synchronous methods (based on requests library) as well as as

## 星数曲线

```mermaid
xychart-beta
    title "wwakabobik/leonardo_api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-31 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `bfa18843becc` · [字段定义](../../DATASET.md)*
