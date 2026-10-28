# Qtty/jadx-mcp-server

⭐ 33 · Java · 推送 2026-08-20 · [GitHub](https://github.com/Qtty/jadx-mcp-server) · 个人维护

**把 JADX 反编译能力封装成 MCP 工具的 Android 逆向服务器**

面向安全研究者的 MCP 服务器：通过两进程架构（Python MCP 层 + 常驻 JVM 反编译守护进程，localhost HTTP 通信）向 Claude 等 AI 助手暴露 APK 分析工具，包括反编译源码、类/方法/字段检索、组件提取、跨引用与继承层级、全 APK sink 扫描、smali 提取等。JVM 守护进程跨会话保持 APK 已加载状态，避免重复解析。构建需 Java 17+、Maven 3.6+ 与 Python 3.10+，工具输出多设默认上限（1000 条/8KB）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python MCP 层 + 常驻 JVM 守护进程的两进程架构，APK 跨会话保持加载
- 跨引用/继承工具读取 dex 反向索引，可将接口分派解析到具体实现
- 按影响类别分类的全 APK 框架 sink 调用点扫描，无需反编译
- 各工具输出设默认上限（类列表/源码字节/xref 条目）并提供 limit/maxBytes 逃生口

## 适用场景

- 安全研究者让 Claude 等 AI 助手直接分析 Android APK
- 程序化逆向：检索类、方法、跨引用并定位恶意/敏感调用点
- 提取 AndroidManifest 导出组件与入口 Activity 做安全评估

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server that provides Android APK reverse engineering capabilities using JADX (Java An
> L8: Claude ──stdio──►  mcp_server/jadx_mcp.py  ──HTTP──►  JVM daemon (JADX)

## 星数曲线

```mermaid
xychart-beta
    title "Qtty/jadx-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-28 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9c5f8db642e9` · [字段定义](../../DATASET.md)*
