# ysfemreAlbyrk/ollama-monitor

⭐ 31 · Go · 推送 2026-06-03 · [GitHub](https://github.com/ysfemreAlbyrk/ollama-monitor) · 个人维护

**系统托盘应用：实时监控本机 Ollama 模型运行状态**

用 Go 编写的跨平台系统托盘应用，面向运行 Ollama 的用户：实时追踪已加载模型并在托盘菜单逐行展示，提供模型状态变化桌面通知、颜色编码状态图标（绿=模型运行/蓝=空闲/红=离线）、Windows 开机自启开关，以及可自定义 API URL（支持 HTTPS 代理与跳过 SSL/TLS 校验）。要求 Go 1.18+ 与已安装的 Ollama。提供预编译可执行文件下载，或经 build.bat / go build 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时追踪已加载的 Ollama 模型，托盘菜单按模型分行展示
- 模型状态变化的桌面通知与颜色编码图标
- 可配置 API URL，支持 HTTPS 代理与 SSL/TLS 校验跳过
- Windows 开机自启托盘原生选项

## 适用场景

- 在后台随时查看本机 Ollama 是否有模型在加载运行
- Ollama 服务离线时收到桌面通知
- 通过托盘快速切换要连接的 Ollama API 地址

## 场景标签

 · 领域:LLM 运维/监控

## 证据(README 行号)

> L7: A lightweight cross-platform system tray application to monitor Ollama AI models with real-time status updates and z
> L13: - 🔄 **Real-Time Monitoring**: Dynamic tracking of loaded Ollama models.

## 星数曲线

```mermaid
xychart-beta
    title "ysfemreAlbyrk/ollama-monitor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8533d427d605` · [字段定义](../../DATASET.md)*
