# a-Fig/Accordion

⭐ 247 · TypeScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/a-Fig/Accordion) · [官网](https://get-accordion.dev) · 个人维护

**pi 编码 agent 的上下文窗口可视化与折叠管理扩展**

Accordion 是 pi 编码 agent 的扩展，提供浏览器 UI 与 Tauri+SvelteKit 桌面应用，把 agent 的整个上下文窗口按块（用户消息/回复/思考/工具调用与结果）可视化，支持手动或通过五种 Conductor 策略（thermocline、triptych、doorman、handoff、compaction-naive）折叠/展开/固定块，近 ~20k token 为受保护工作尾部。折叠可逆、带确定性摘要摘要缓存，无需向量数据库。桌面应用含 Claude Code 转录只读浏览。基准为单次 hackathon 规模运行，作者自述尚非可发布评测；agent 驱动固定、嵌套分组、回放功能未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 上下文 Map 按块可视化（token 权重骰面 1-6、类型着色）
- 五种 Conductor 自动折叠策略，折叠可逆且近 ~20k token 受保护
- 多会话侧栏与实时联动 pi 会话（自动发现）
- 浏览器 UI（npm 包即可）与桌面应用（Tauri，需 Node 20+ 与 Rust）两种形态

## 适用场景

- 长会话中查看并手工管理 agent 上下文占用
- 用 thermocline/triptych 等策略自动压缩上下文以延长会话
- 只读浏览已保存的 Claude Code 转录（桌面应用）

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13: Accordion is a pi extension that shows you
> L141: - ✅ Live link to a running pi session, with auto-discovery.
> L144: - ✅ Reversible, provider-safe folding with deterministic `{#code FOLDED}` digests the

## 星数曲线

```mermaid
xychart-beta
    title "a-Fig/Accordion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 245 --> 248
    line [246, 247, 247]
```

2026-10-18 246 → 2026-10-29 247（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `491de771e5fd` · [字段定义](../../DATASET.md)*
