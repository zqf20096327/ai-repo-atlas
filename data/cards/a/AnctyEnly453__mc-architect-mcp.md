# AnctyEnly453/mc-architect-mcp

⭐ 20 · Java · MIT · 推送 2026-09-06 · [GitHub](https://github.com/AnctyEnly453/mc-architect-mcp) · 个人维护 · 中文 README

**让 AI 在 Minecraft 存档中设计、施工与调试建筑的 MCP 服务器与 Fabric Mod**

由 Fabric Mod（世界读写端）与 Node.js MCP bridge（AI 客户端接入端）组成：AI agent 通过 9 个 MCP 工具（mc_world/mc_workspace/mc_edit/mc_build/mc_inspect/mc_camera/mc_test/mc_redstone/mc_keyboard）操作 Minecraft Java 1.21.11 单人存档，实现模块化建筑设计、增量施工与回滚、地形/照明/通行检查、旁观相机截图验收、红石信号采样与波形调试，以及可选的独立红石加速。设计以本地 JSON 保存；离线预览不模拟红石。需要 Java 21+ 与 Node.js 22+，从 Releases 安装 Mod 并从源码构建 bridge。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 个 MCP 工具覆盖世界管理、模块编辑、增量施工、检查、相机截图与红石测试
- 施工支持暂停/恢复/回滚与冲突检查，只改动需要变化的方块
- 红石输入序列、真实信号采样、断言与波形调试，可选红石加速
- Mod 仅监听 127.0.0.1 并使用随机 Token 认证

## 适用场景

- 让 AI agent 在我的单人存档里按模块设计并施工大型建筑
- 对 AI 生成的建筑用截图、通行与照明检查做验收
- 调试与验收红石电路：输入序列、信号断言和波形

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: # MC Engineer · Minecraft 建筑 MCP
> L5: 让 AI 在 **Minecraft Java 1.21.11** 的单人存档里设计、修改和调试建筑与红石工程。项目原名 MC Architect MCP，仓库地址与 Mod ID `mcarchitect` 保持不变。
> L66: 通常从 `mc_world context` 开始，用返回的世界身份创建工程。设计分成命名模块，先规划和预览，再部署并查询状态。建筑用游戏截图和通行检查验收，红石电路用真实信号测试验收。

## 星数曲线

```mermaid
xychart-beta
    title "AnctyEnly453/mc-architect-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c3ea8e7f23fd` · [字段定义](../../DATASET.md)*
