# sarang-cmd/perplexity-autorename

⭐ 3 · JavaScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sarang-cmd/perplexity-autorename) · [官网](perplexity-autorename.vercel.app) · 个人维护

**给 Perplexity 用户自动把会话重命名为 3-7 词标题的 Chrome 扩展**

Chrome Manifest V3 浏览器扩展：在 Perplexity.ai 新会话首条回答流式结束后，将线程重命名为 3-7 词的简洁标题并写入 Perplexity 账户，实现多端侧边栏同步。机制上通过 MAIN world 注入脚本用 Response.body.tee() 克隆 SSE 流，解析内部 context_uuid 与 read_write_token 后调用重命名接口；标题由 10 个可选 LLM 提供商生成，或使用内置离线关键词启发式（无 API key、无网络调用）。支持批量清理历史会话、正则排除规则、检测手动重命名并锁定。需在 Chrome/Brave/Arc/Edge 中以开发者模式加载。

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

- 拦截并克隆 Perplexity SSE 流，解析内部令牌完成重命名（HTTP 204 持久化）
- 10 个 LLM 提供商可选，含本地 Ollama/LM Studio/vLLM 自定义端点
- 无 API key 的离线确定性关键词标题生成模式
- 批量重命名历史会话（Past 50/20 Chats、自定义范围）与正则排除规则

## 适用场景

- 整理 Perplexity 侧边栏里被截断的原始会话标题
- 研究冲刺时用 [Research]/[Paper] 前缀对主题做视觉分组
- 粘贴长堆栈调试后让线程获得可读标题
- 离线/气隙环境下用本地模型或启发式生成标题

## 场景标签

 · 领域:浏览器工具/效率工具

## 证据(README 行号)

> L35: **Auto-Rename for Perplexity** watches only the **first answer** of a brand-new thread on `https://www.perplexity.a
> L68: 4. **100% Local / Air-Gapped Mode (Ollama, LM Studio, or Offline Heuristic):**

## 星数曲线

```mermaid
xychart-beta
    title "sarang-cmd/perplexity-autorename 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `398a1e2041bc` · [字段定义](../../DATASET.md)*
