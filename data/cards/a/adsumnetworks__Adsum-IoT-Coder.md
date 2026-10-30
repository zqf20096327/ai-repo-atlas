# adsumnetworks/Adsum-IoT-Coder

⭐ 27 · TypeScript · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/adsumnetworks/Adsum-IoT-Coder) · [官网](https://www.adsumnetworks.com) · 组织维护

**面向嵌入式 IoT 固件的 VS Code AI 编码代理（ESP32/nRF）**

Adsum Networks 开发的 VS Code 扩展：在 Espressif ESP-IDF 与 Nordic nRF Connect SDK（Zephyr）工具链上构建、烧录、调试固件，读取 RTT/UART 串口日志，关联 HCI 与空口抓包调试 BLE，发送 AT/shell 命令并解码调制解调器跟踪。附 EU 网络弹性法案（CRA）就绪检查：生成 SPDX SBOM、扫描 EUVD/NVD/OSV CVE、核查安全启动/签名更新等配置。支持自选模型（Ollama、Claude、DeepSeek 等）。蜂窝/NB-NTN/LoRa/边缘 AI 功能需免费注册账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在真实硬件上构建、烧录、调试，含 RTT/UART 实时日志与 BLE 空口抓包关联
- CRA 就绪检查：SPDX SBOM、EUVD/NVD/OSV CVE 扫描、安全配置核查与修复建议
- 支持 Fanstel BLG20x/LBG20x 网关的配对、认领、双处理器升级与开通
- 项目记忆存于 .adsum/，可导出为单个脱敏文件

## 适用场景

- 在 VS Code 中调试 ESP32/nRF 固件的 BLE 与崩溃问题
- 为固件构建生成 SBOM 并做 CVE 扫描，准备 CRA 合规
- 通过卫星 NB-NTN/LTE-M 将蓝牙设备数据经 Fanstel 网关上云

## 场景标签

`编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L5: **A coding agent for IoT firmware on Espressif ESP and Nordic nRF. It works in VS Code: it builds and flashes your p
> L62: ## What it does

## 星数曲线

```mermaid
xychart-beta
    title "adsumnetworks/Adsum-IoT-Coder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cdb3d7fac9f7` · [字段定义](../../DATASET.md)*
