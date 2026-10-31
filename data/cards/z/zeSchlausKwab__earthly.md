# zeSchlausKwab/earthly

⭐ 15 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/zeSchlausKwab/earthly) · [官网](https://earthly.city) · 个人维护

**基于 Nostr 的协作地图编辑器，含 AI 制图助手与离线能力**

Earthly.city 是运行于 Web 与 Android 的协作式地图编辑器：支持触控 GeoJSON 绘制编辑、将版本化地理实体发布到 Nostr 中继、群组策展数据集、几何感知评论、MLS 加密私群与附近设备离线同步（Android 内嵌 Nostr 中继与 Blossom 服务器）。AI 部分：编辑器内映射助手可调用类型化工具创建几何、经 ContextVM/MCP 使用远程工具与 QuickJS 地理沙箱、受控批量编辑与文件导入。技术栈为 Bun/React 19/Tauri 2/Rust/Go，需从源码构建，Android 为发布目标，桌面分发暂缓。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GeoJSON 绘制编辑并发布版本化地理实体到 Nostr 中继
- 编辑器内 AI 制图助手：类型化工具、ContextVM/MCP、QuickJS 地理沙箱
- MLS 加密私群与附近设备局域网离线同步
- Android 内嵌本地 Nostr 中继与 Blossom 服务器

## 适用场景

- 将本地地理知识绘制成可共享的公开地图数据集
- 团队/社群在群组中围绕地点协作、评论与提交编辑提案
- 无可靠网络的野外场景下用多台手机就近同步地图与文件
- 借助 AI 助手把地理研究整理为结构化可审阅的地图内容

## 场景标签

 · 领域:地理空间/协作地图

## 证据(README 行号)

> L3: Earthly is a collaborative map editor built on Nostr that helps people turn local knowledge into useful, shared maps
> L29: - ✨ AI-assisted mapping with typed editor tools, remote ContextVM/MCP tools, guarded bulk edits, file ingest, and a

## 星数曲线

```mermaid
xychart-beta
    title "zeSchlausKwab/earthly 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `476d5eedd7e0` · [字段定义](../../DATASET.md)*
