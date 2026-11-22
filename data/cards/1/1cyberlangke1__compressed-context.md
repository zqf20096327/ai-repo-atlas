# 1cyberlangke1/compressed-context

⭐ 3 · TypeScript · MIT · 推送 2026-11-16 · [GitHub](https://github.com/1cyberlangke1/compressed-context) · 个人维护 · 中文 README

**OpenCode 上下文压缩插件：把旧对话折叠成摘要块延长会话**

面向 OpenCode 的上下文压缩插件：将较早对话历史折叠为自包含摘要块（T1），摘要块超预算时自动向 T2/T3 递归合并，原始消息移入持久化存储以释放上下文窗口；模型可通过 compress/decompress 工具主动打检查点或按需还原历史。支持按模型覆盖阈值、markdown/babel 双摘要格式、保持前缀以兼容 Prompt Cache，并提供 TUI 面板查看摘要块与配置。通过 npm 分发，OpenCode 启动时自动安装，建议同时关闭 OpenCode 原生自动压缩。

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

- 递归分层折叠：T1 压缩原始对话，超预算自动合并为 T2/T3 滚动累积块
- compress/decompress 工具：模型可主动打检查点或逐层/完整还原历史
- TUI 面板查看摘要块、缓存命中率，并可修改配置与检查更新
- 按模型单独覆盖 6 个 token 相关阈值参数

## 适用场景

- 在有限上下文窗口里让 OpenCode 长会话继续运行
- 按所用模型（如 200K/1M 窗口）分别设置压缩触发阈值
- 需要时按块回溯已被压缩的历史对话

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: OpenCode 的上下文压缩插件。它会将较早的对话历史折叠成独立的摘要块，让长会话在有限的上下文窗口里继续跑下去。
> L13: 插件接管发给模型的上下文：把较早的对话折叠成摘要块，让长会话继续跑下去：
> L45: 插件通过 npm 分发，OpenCode 启动时会自动安装。

## 星数曲线

```mermaid
xychart-beta
    title "1cyberlangke1/compressed-context 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-24 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `181b3d05b9b3` · [字段定义](../../DATASET.md)*
